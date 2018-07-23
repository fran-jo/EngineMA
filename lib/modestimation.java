package fileconversion;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

import matlabcontrol.MatlabConnectionException;
import matlabcontrol.MatlabInvocationException;
import matlabcontrol.MatlabProxy;
import matlabcontrol.MatlabProxyFactory;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;


public class modestimation extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args)throws MatlabConnectionException, MatlabInvocationException {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					modestimation frame = new modestimation();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public modestimation() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JButton btnNewButton = new JButton("Mode Estimation");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			MatlabProxyFactory factory = new MatlabProxyFactory();
				    try {
				    	File file = new File("C:/Users/fragom/PhD_CIM/PYTHON/ScriptMAE/lib/file.txt");
						FileReader fileReader = new FileReader(file);
						BufferedReader bufferedReader = new BufferedReader(fileReader);
						StringBuffer stringBuffer = new StringBuffer();
						String line;
						while ((line = bufferedReader.readLine()) != null) {
							stringBuffer.append(line);
							stringBuffer.append("\n");
						}
						fileReader.close();
						//System.out.println("Contents of file:");
						
						//System.out.println(stringBuffer.toString());
						
				    	
				    	MatlabProxy proxy = factory.getProxy();
						//proxy.eval("data = h5read('PMUdata_Bus1VA2VALoad9PQ.h5','/df/block0_values');");
				    	proxy.eval(stringBuffer.toString());
						proxy.eval("runhh5");
						//proxy.eval("exit");
						proxy.disconnect();
						
					} catch (MatlabConnectionException | MatlabInvocationException | IOException e1) {
						// TODO Auto-generated catch block
						e1.printStackTrace();
					}


				
			}
		});
		btnNewButton.setBounds(144, 95, 158, 61);
		contentPane.add(btnNewButton);
	}
}
